class User:
    ADMIN_ROLE = 'admin'
    EMPLOYEE_ROLE = 'employee'
    CUSTOMER_ROLE = 'customer'
    ALLOWED_ROLES = {ADMIN_ROLE, EMPLOYEE_ROLE, CUSTOMER_ROLE}
    all_user_ids = set()

    def __init__(self, name, role, user_id=None):
        self.validate_role(role)   # Ensure that the role has an allowed value
        if user_id:
            self.user_id = user_id
        elif User.all_user_ids:
            self.user_id = max(User.all_user_ids) + 1
        else:
            self.user_id = 1
        self.validate_id(self.user_id)  # Ensure that the id is a unique integer
        self.name = name
        self.role = role
        self.log_user_creation()
        User.all_user_ids.add(self.user_id)

    @classmethod
    def is_valid_role(cls, role):
        # TODO: Update this to correctly implement role checking logic
        return role in cls.ALLOWED_ROLES

    @classmethod
    def is_unique(cls, user_id):
        return user_id not in cls.all_user_ids

    def log_user_creation(self):
        self.log("User", self.user_id, "-", self.name, "created with role:", self.role)

    @staticmethod
    def log(*args):
        print("USER LOG: ", *args)

    @classmethod
    def create_customer(cls, name):  # Uses the factory pattern - common in Java
        return cls(name, cls.CUSTOMER_ROLE)

    # Validation Methods
    # ~~~~~~~~~~~~~~~~~~
    @classmethod
    def validate_role(cls, role):
        """Raise an exception if role does not have an allowed value"""
        if not cls.is_valid_role(role):
            cls.log(role, "is not a valid role")
            raise ValueError("Invalid role")

    @classmethod
    def validate_id(cls, user_id):
        """Raises an exception if user_id is not a unique integer"""
        if not isinstance(user_id, int):
            cls.log("User id", user_id, "is not an integer")
            raise TypeError("user_id should be an integer")

        if not cls.is_unique(user_id):
            cls.log("User cannot be created with a non unique id:", user_id)
            raise ValueError(f"User id is not unique")
