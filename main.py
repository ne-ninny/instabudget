def monthly_budget(annual_budget):
    print(" ")
    print("============================== INSTABUDGET ==============================")
    print(f"Here's your budget based on your ${annual_budget} a year budget!: ")

    print("""
           SAVINGS (40%): 
           HOUSING (20%):
    TRANSPORTATION (10%):
              FOOD (10%):
     HEALTH/MEDICAL (5%):
          UTILITIES (3%):
          WHATEVER (10%):
          
             TOTAL (98%):
          LEFT OVER (2%):
          """)




introduction = input("Please provide a name: ") 
annual_salary = input(f"Hello, {introduction}! What is your annual salary?: ")

monthly_budget(annual_salary)