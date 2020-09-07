import pandas as pd
import os

def main(input_data):
    print('########################(START)############################')
    #input files
    case_over = pd.read_csv(r'MIGHTY CSV files/CASE OVERVIEW 8-31-2020.csv')
    contact = pd.read_csv(r'MIGHTY CSV files/CONTACTS 8-31-2020.csv')
    lawfirm = pd.read_csv(r'MIGHTY CSV files/LAWFIRM 8-31-2020.csv')
    plaint = pd.read_csv(r'MIGHTY CSV files/PLAINTIFF 8-31-2020.csv')

    df = pd.DataFrame()

    print('>>>>>>>>>> CASE OVERVIEW 8-31-2020.csv')
    for i in case_over:
        if i == 'first_name':
            df['First Name'] = case_over['first_name']
        elif i == 'last_name':
            df['Last Name'] = case_over['last_name']
        elif i == 'birthdate':
            df['Birth Date'] = case_over['birthdate']
        elif i == 'sex':
            df['Sex'] = case_over['sex']
        elif i == 'address1':
            df['Address1'] = case_over['address1']
        elif i == 'address2':
            df['Address2'] = case_over['address2']
        elif i == 'city':
            df['City'] = case_over['city']
        elif i == 'state_id':
            df['State ID'] = case_over['state_id']
        elif i == 'zip_code':
            df['Zip Code'] = case_over['zip_code']    
        elif i == 'email':
            df['Email'] = case_over['email']
        elif i == 'phone_number':
            df['Phone Number'] = case_over['phone_number']
        elif  i == 'date_of_loss':
            df['Date of Loss'] = case_over['date_of_loss']
        elif  i == 'case_closed_date':
            df['Case Closed Date'] = case_over['case_closed_date']
        elif i == 'tracking_follow_up_date':
            df['Tracking Follow up Date'] = case_over['tracking_follow_up_date']
        elif i == 'current_status':
            df['Current Status'] = case_over['current_status']
        elif i == 'current_medical_status':
            df['Current Medical Status'] = case_over['current_medical_status']
        elif i == 'current_attributes':
            df['Current Attributes'] = case_over['current_attributes']
        elif i == 'case_tracking_note':
            df['Case Tracking Note'] = case_over['case_tracking_note']
        elif i == 'case_return_status':
            df['Case Return Status'] = 'case_return_status'
        elif i == 'latest_date_closed':
            df['Latest Date Closed'] = case_over['latest_date_closed']
        elif i == 'date_of_last_payment':
            df['Date of Last Payment'] = case_over['date_of_last_payment']
        elif i == 'payment_notes':
            df['Payment Notes'] = case_over['payment_notes']
        elif i == 'returned_amount':
            df['Returned Amount'] = case_over['returned_amount']
        elif i == 'application_status':
            df['Application Status'] = case_over['application_status']
        elif i == 'agreement_date':
            df['Agreement Date'] = case_over['agreement_date']
        elif i == 'funded_date':
            df['Funded Date'] = case_over['funded_date']
        else:
            new = i.capitalize()
            df[new] = case_over[i]

    print('>>>>>>>>>> CONTACTS 8-31-2020.csv')
    for item in contact.columns.values:
        if item == 'contact_id':
            df['Contcat Id'] =  contact['contact_id']
        elif item == 'full_name':
            df['Full Name'] =  contact['full_name'] 
        elif item == 'link_to_contact':
            df['Link to Contact'] =  contact['link_to_contact']
        elif item == 'phone_number':
            df['Phone Number'] =  contact['phone_number']
        elif item == 'cell_number':
            df['Cell Number'] =  contact['cell_number']
        elif item == 'fax_number':
            df['Fax Number'] =  contact['fax_number']
        elif item == 'law_firm':
            df['Law Firm'] =  contact['law_firm']
        elif item == 'email':
            df['Email'] =  contact['email']
        elif item == 'law_firm':
            df['Law Firm'] =  contact['law_firm']

    print('>>>>>>>>>> LAWFIRM 8-31-2020.csv')
    for item in lawfirm.columns.values:
        if item == 'lawfirm_id':
            df['Lawfirm Id'] =  lawfirm['lawfirm_id']
        if item == 'name':
            df['Name of Law Firm'] =  lawfirm['name']
        if item == 'phone_number':
            df['Phone Number'] =  lawfirm['phone_number']
        if item == 'fax_number':
            df['Fax Number'] =  lawfirm['fax_number']
        if item == 'address':
            df['Address'] =  lawfirm['address']
        if item == 'website':
            df['Website'] =  lawfirm['website']
        if item == 'summary':
            df['Summary'] =  lawfirm['summary']


    print('>>>>>>>>>> PLAINTIFF 8-31-2020.csv')
    for item in plaint.columns.values:
        if item == 'plaintiff_id':
            df['Plaintiff Id'] =  plaint['plaintiff_id']
        if item == 'plaintiff_name':
            df['Plaintiff Name'] =  plaint['plaintiff_name']
        if item == 'link_to_case':
            df['Link to Case'] =  plaint['link_to_case']
        if item == 'phone_number':
            df['Phone Number'] =  plaint['phone_number']
        if item == 'email':
            df['Plaintiff Id'] =  plaint['email']
        if item == 'address':
            df['Address'] =  plaint['address']
        if item == 'birthdate':
            df['Birthdate'] =  plaint['birthdate']
        if item == 'sex':
            df['Sex'] =  plaint['sex']

    df1 = pd.DataFrame()
    #output should be
    opportunities = pd.read_csv(r'Zoho CRM Modules/Opportunities.csv')
    contact_out = pd.read_csv(r'Zoho CRM Modules/Contacts_001.csv')
    organization = pd.read_csv(r'Zoho CRM Modules/Organization.csv')

    if 'opportunities.csv' == input_data: 
        print('>>>>>>>>>> Opportunities.csv')
        for i in opportunities.columns.values:
            for j in df.columns.values:
                try:
                    if j == i.capitalize():
                        print(j)
                        df1[j] = df[j]
                except Exception as e:
                    print(e)
        print('Match found!!')
    elif 'Contacts_001.csv' == input_data:
        print('>>>>>>>>>> Contacts_001.csv')
        for i in contact_out.columns.values:
            for j in df.columns.values:
                if j == i.capitalize():
                    print(j)
                    df1[j] = df[j]
        print('Match found!!')
    elif 'Organization.csv' == input_data:
        print('>>>>>>>>>> Organization.csv')
        for i in organization.columns.values:
            for j in df.columns.values:
                if j == i.capitalize():
                    print(j)
                    df1[j] = df[j]
        print('Match found!!')
                        
    print('########################(END)############################')
    df1.to_csv('output.csv')
    print(df1.head())
    return 'output.csv'
     


if __name__ == "__main__":
    import ipywidgets
    ipywidgets.RadioButtons(
        options=['pepperoni', 'pineapple', 'anchovies'],
    #     value='pineapple',
        description='File you want:',
        disabled=False
    )
    input_data = input('Enter File that you want : ')
    file_loc = main(input_data)
    print(os.path.abspath(file_loc))
