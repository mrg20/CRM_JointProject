from CRMapp.WebUserController import WebUserController


class CompanyController(WebUserController):
    def get_company_profile_parameters(self, request):
        """
        Capture the parameters of the company type user profile
        :param request: HttpRequest
        :return: A dictionary with parameters
        """
        parameters = {}
        self.get_basic_parameters(parameters, request)
        self.get_user_parameters(parameters, request)
        self.get_category_parameters(parameters, request)
        self.get_company_parameters(parameters, request)
        return parameters

    def get_company_parameters(self, parameters, request):
        """
        Captures the parameters associated with the UserAsCompany model
        :param parameters: The dictionary where the parameters will be stored
        :param request: HttpRequest
        """
        # company information
        parameters['cif'] = request['cif']

    def update_company_profile(self, parameters, user, web_user, user_as_company):
        """
        Update user profile of company type
        :param parameters: Dictionary that contains all the parameters
        :param user: Django user model
        :param web_user: WebUser model
        :param user_as_company: UserAsCompany model
        """
        self.update_basic_parameters(parameters, user)
        self.update_user_parameters(parameters, web_user)
        self.update_category_parameters(parameters, web_user)
        self.update_company_parameters(parameters, user_as_company)
        user.save(update_fields=["username", "email"])
        web_user.save(update_fields=["country", "province", "city", "zip_code",
                                     "street", "phone"])
        user_as_company.save(update_fields=["CIF"])

    def update_company_parameters(self, parameters, user_as_company):
        """
        Updates the parameters associated with the UserAsCompany model
        :param parameters: Dictionary that contains all the parameters
        :param user_as_company: UserAsCompany model
        """
        user_as_company.CIF = parameters['cif']

    def create_new_company_user(self, user_as_company_form, web_user):
        new_company_user = user_as_company_form.save(commit=False)
        new_company_user.web_user = web_user
        new_company_user.save()
