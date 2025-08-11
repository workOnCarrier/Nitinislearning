problem = '''
Part 1
There are several brands of vaccinations. The list of brands and the number of doses required for full vaccination is as follows:
Brand Doses Needed
PZ 2
MD 2
CV 2
JJ 1

 
The criteria for a status of vaccinated are that
the number of doses administered is equal to or greater than the number of doses needed for the relevant brand, and
for brands which require two doses, consecutive doses of the same brand are administered i.e. there is no other dose administered on a day between the two doses
Input:
An array of doses administered
Each dose is an array of brand and date, e.g. ['PZ', 12]
The date of vaccination is a single integer representing the number of days after 1 Jan 2021
The dose records will not necessarily be in order according to date
It is guaranteed that the brands will be a valid brand from the table
It is guaranteed that no two vaccines will be taken on the same date

Implement a function, isVaccinated which takes the dose array input, and outputs a string vaccinated or not_vaccinated

isVaccinated([['PZ', 30], ['PZ', 47]]) 		   		    // 'vaccinated'
isVaccinated([['MD', 30], ['CV', 40], ['MD', 37]]) 		    // 'vaccinated'
isVaccinated([['JJ', 10], ['CV', 35]]) 		   		    // 'vaccinated'
isVaccinated([['CV', 10], ['CV', 17], ['MD', 35]])   		    // 'vaccinated'
isVaccinated([['PZ', 30], ['PZ', 73], ['MD', 48], ['MD', 105]]) // 'not_vaccinated'
'''

# Brand Doses Needed
# PZ 2
# MD 2
# CV 2
# JJ 1

def check_if_vaccinated(curr_vac_status: dict):
    req_table = {'PZ': 2, 'MD': 2, 'CV': 2, 'JJ': 1}
    for key, value in curr_vac_status.items():
        if req_table[key] == value:
            return True
    return False

def check_if_vaccinated_updated(cur_vac, cur_vac_count):
    req_table = {'PZ': 2, 'MD': 2, 'CV': 2, 'JJ': 1}
    if cur_vac in req_table.keys():
        if cur_vac_count >= req_table[cur_vac]:
            return True
    return False

def invalidate_other_vaccines(curr_vac_status: dict, value):
    for key, val in curr_vac_status.items():
        if key != value:
            curr_vac_status[key] = 0

def isVaccinated_fail(input: list):
    date_vac_seq = {}
    sorted_date_vac_seq = {}
    # print(f"input:{input}")
    for entry in input:
        vac = entry[0]
        date = entry[1]
        date_vac_seq[date] = vac
    # print(date_vac_seq)
    sorted_keys = list(date_vac_seq.keys())
    sorted_keys.sort()
    sorted_date_vac_seq = { i: date_vac_seq[i] for i in sorted_keys}
    # print(f"sorted: {sorted_date_vac_seq}") # by date

    cummulative_vacc = {}
    for key, value in sorted_date_vac_seq.items():
        if value not in cummulative_vacc:
            cummulative_vacc[value] = 0
        cummulative_vacc[value] += 1
        # print(f"cumm_vacc:{cummulative_vacc}")
        invalidate_other_vaccines(cummulative_vacc, value)
        if check_if_vaccinated(cummulative_vacc):
            return "vaccinated"
        # print(f"\t cumm_vacc:{cummulative_vacc}")
    return "not_vaccinated"

def isVaccinated(input: list):
    date_vac_seq = {}
    sorted_date_vac_seq = {}
    # print(f"input:{input}")
    for entry in input:
        vac = entry[0]
        date = entry[1]
        date_vac_seq[date] = vac
    # print(date_vac_seq)
    sorted_keys = list(date_vac_seq.keys())
    sorted_keys.sort()
    sorted_date_vac_seq = { i: date_vac_seq[i] for i in sorted_keys}
    # print(f"sorted: {sorted_date_vac_seq}") # by date

    cur_vac = ""
    cur_vac_count = 0
    for key, value in sorted_date_vac_seq.items():
        if value != cur_vac:
            cur_vac = value
            cur_vac_count = 1
        else:
            cur_vac_count += 1
        # print(f"cumm_vacc:{cummulative_vacc}")
        if check_if_vaccinated_updated(cur_vac, cur_vac_count):
            return "vaccinated"
        # print(f"\t cumm_vacc:{cummulative_vacc}")
    return "not_vaccinated"
    

def isVaccinated_ai(doses):
    # Doses required for each brand
    req = {'PZ': 2, 'MD': 2, 'CV': 2, 'JJ': 1}
    # Sort doses by date
    doses_sorted = sorted(doses, key=lambda x: x[1])
    n = len(doses_sorted)
    # Try all possible windows for each brand
    for brand, needed in req.items():
        # Get all doses of this brand, in order
        brand_doses = [d for d in doses_sorted if d[0] == brand]
        if len(brand_doses) < needed:
            continue
        if needed == 1:
            # JJ: just need one dose
            if brand == 'JJ' and len(brand_doses) >= 1:
                return "vaccinated"
            # For other brands, continue
        else:
            # For 2-dose brands, check all pairs of doses of this brand
            for i in range(len(brand_doses) - 1):
                d1 = brand_doses[i][1]
                d2 = brand_doses[i+1][1]
                # Find indices in the full sorted list
                idx1 = next(j for j, d in enumerate(doses_sorted) if d == brand_doses[i])
                idx2 = next(j for j, d in enumerate(doses_sorted) if d == brand_doses[i+1])
                # Check if all doses between idx1 and idx2 are of the same brand
                if all(doses_sorted[j][0] == brand for j in range(idx1, idx2+1)):
                    return "vaccinated"
    return "not_vaccinated"

# Example usage and test
def test():
    # print(isVaccinated([['PZ', 30], ['PZ', 47]])) 		   		    #// 'vaccinated'
    print(isVaccinated([['MD', 30], ['CV', 40], ['MD', 37]])) 		 #   // 'vaccinated'

def final_test():
    print(isVaccinated([['PZ', 30], ['PZ', 47]])) 		   		    #// 'vaccinated'
    print(isVaccinated([['MD', 30], ['CV', 40], ['MD', 37]])) 		 #   // 'vaccinated'
    print(isVaccinated([['JJ', 10], ['CV', 35]])) 		   		    #// 'vaccinated'
    print(isVaccinated([['CV', 10], ['CV', 17], ['MD', 35]]))   		    #// 'vaccinated'
    print(isVaccinated([['PZ', 30], ['PZ', 73], ['MD', 48], ['MD', 105]])) #// 'not_vaccinated'

if __name__ == "__main__":
    final_test()