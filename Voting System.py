def voter_ID(used_id):
    result = []
    
    while True:
        id = input("Enter your Voter ID (Type exit to leave the program): ")
        if id in used_id:
            print("The ID entered has already been used.")
            continue
        if id.lower() == 'exit':
            print("exiting the program....")
            exit()
        user = input("Enter your Name: ")
        if "ID" in id and len(id) < 7:
            result.append("---------------------- User Name: {} |::| User Voter ID: {} -----------------------".format(id, user))
            used_id.append(id)
            break
        else:
            print("Invalid Voter ID or Name")
            break
    
    return result
def candidate():
    vote = {'Kaashif': 0, 'Amir': 0, 'Hassan': 0, 'Alia': 0}
    used_id = []  
    while True:
        voter_data = voter_ID(used_id)
        if voter_data: 
            print(voter_data)  
            print("The Candidates are:\n |.Kaashif |\n |.Amir    |\n |.Tom     |\n |.Hassan  |\n |.Alia    |")
            pick_candi = input("Enter the candidate you want to vote for: ").capitalize()
            if pick_candi in vote:
                vote[pick_candi] += 1  
                print("Vote casted for {}. Current votes: {}".format(pick_candi, vote))
                
            else:
                print("The entered candidate does not exist.")
                break
        else:
            print("No valid voter ID entered. Exiting the voting process.")
            break  


candidate()
