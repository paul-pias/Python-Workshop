from rds import Admin

admin_person = Admin("Tarek", 20)
admin_person.add_info("Emran", 10, "summer", "cse")

print(admin_person.info())