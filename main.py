def monthly_budget(annual_budget):
    one_month = annual_budget / 12
    
    print(" ")
    print("============================== INSTABUDGET ==============================")
    print(f"Here's your budget based on your ${annual_budget} a year budget!: ")
    
    print(f"""
           SAVINGS (40%): ${one_month * 0.4}
           HOUSING (20%): ${one_month * 0.2}
    TRANSPORTATION (10%): ${one_month * 0.1}
              FOOD (10%): ${one_month * 0.1}
     HEALTH/MEDICAL (5%): ${one_month * 0.05}
          UTILITIES (3%): ${one_month * 0.03}
          WHATEVER (10%): ${one_month * 0.1}
          
             TOTAL (98%): ${one_month * 0.98}
          LEFT OVER (2%): ${one_month * 0.02}
          """)
# 
# 
# 

introduction = input("Please provide a name: ") 
annual_salary = input(f"Hello, {introduction}! What is your annual salary?: ")

monthly_budget(100000)