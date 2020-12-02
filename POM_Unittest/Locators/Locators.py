class locator():
    #All locators

    text_Username_Id  = "Email"
    text_password_Id = "Password"
    bttn_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    logout_linktext = "logout"

    # Main page
    header_Plinktxt = "Play sample applicat"
    filterbyName_textfield_Id = "searchbox"
    filerbyName_button_Id = "searchsubmit"
    add_new_computer_Id = "add"
    computername_linktxt = "Computer name"
    Introduced_linktxt = "Introduced"
    Discontinued_linktxt = "Discontinued"
    company_linktxt = "Company"
    table_xpath = "//*[@id='main']/table/tbody"
    row_tag_name = "tr"
    col_tag_name = "td"
    ace_linktext = "ACE"

    # Edit Computer Page
    company_dropdown_Id = "company"
    save_button_xpath = "//*[@id='main']/form[1]/div/input"
    delete_button_xpath = "//*[@id='main']/form[2]/input"

    # Add new computer page
    heading_label_xpath = "//*[@id='main']/h1"
    header_add_computer_xpath = "//*[@id='main']/h1"
    computername_label_xpath = "//*[@id='main']/form/fieldset/div[1]/label"
    computername_textfield_id = "name"
    introduced_label_xpath = "//*[@id='main']/form/fieldset/div[2]/label"
    intro_date_textfield_id = "introduced"
    discont_date_label_xpath = "//*[@id='main']/form/fieldset/div[3]/label"
    discont_textfield_id = "discontinued"
    company_label_xpath = "//*[@id='main']/form/fieldset/div[4]/label"
    addComputer_button_xpath = "//*[@id='main']/form/div/input"
    cancel_button_xpath = "//*[@id=main]/form/div/a"
