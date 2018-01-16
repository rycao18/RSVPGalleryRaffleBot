    randFirst1 = ""
    randLast1 = ""
    randName11 = ""
    email1 = ""
    randFirst2 = ""
    randLast2 = ""
    randName22 = ""
    email2 = ""
    
    randFirst1 = firstnames[randint(0, len(firstnames) - 1)]
    randLast1 = lastnames[randint(0, len(lastnames) - 1)]
    randName1 = randFirst1 + " " + randLast1
    randFirst2 = firstnames[randint(0, len(firstnames) - 1)]
    randLast2 = lastnames[randint(0, len(lastnames) - 1)]
    randName2 = randFirst2 + " " + randLast2
    email1 = randFirst1
    email2 = randFirst2
    
    for x in range(0, 3):
        email1 += alphanum[randint(0, 35)]
        email2 += alphanum[randint(0, 35)]
    email1 += "@rycao.me"
    email2 += "@rycao.me"
    
    driver1 = webdriver.Chrome()
    driver1.get('https://rsvpgallery.com/pages/raffle')
    driver2 = webdriver.Chrome()
    driver2.get('https://rsvpgallery.com/pages/raffle')
    time.sleep(2)
    
    enterbtn1 = driver1.find_element_by_xpath(
        '//*[@id="content"]/div/div[4]/div/div[2]/div[1]/div')
    enterbtn1.click()
    time.sleep(.5)
    enterbtn2 = driver2.find_element_by_xpath(
        '//*[@id="content"]/div/div[4]/div/div[2]/div[1]/div')
    enterbtn2.click()
    time.sleep(.5)

    nameentry1 = driver1.find_element_by_xpath(
        '//*[@id="raffle_fullname"]')
    nameentry1.send_keys(randName1)
    emailentry1 = driver1.find_element_by_xpath(
        '//*[@id="raffle_email"]')
    emailentry1.send_keys(email1)
    sizeentry1 = driver1.find_element_by_xpath(
        '//*[@id="raffle_form"]/div/div[3]')
    sizeentry1.click()
    size121 = driver1.find_element_by_xpath(
        '//*[@id="raffle_form"]/div/div[3]/ul/li[8]')
    size121.click()
    time.sleep(.5)
    submitbtn1 = driver1.find_element_by_xpath(
        '//*[@id="content"]/div/div[4]/div/div[2]/div[2]/div')
    submitbtn1.click()
    nameentry2 = driver2.find_element_by_xpath(
        '//*[@id="raffle_fullname"]')
    nameentry2.send_keys(randName2)
    emailentry2 = driver2.find_element_by_xpath(
        '//*[@id="raffle_email"]')
    emailentry2.send_keys(email2)
    sizeentry2 = driver2.find_element_by_xpath(
        '//*[@id="raffle_form"]/div/div[3]')
    sizeentry2.click()
    size222 = driver2.find_element_by_xpath(
        '//*[@id="raffle_form"]/div/div[3]/ul/li[8]')
    size222.click()
    time.sleep(.5)
    submitbtn2 = driver2.find_element_by_xpath(
        '//*[@id="content"]/div/div[4]/div/div[2]/div[2]/div')
    submitbtn2.click()

    driver1.close()
    driver1.quit()
    driver2.close()
    driver2.quit()
    time.sleep(randint(2, 5))
    
    print(datetime.now().strftime("%H:%M:%S") + " Submitted Information for " + randName1 + " with email " + email1)
    print(datetime.now().strftime("%H:%M:%S") + " Submitted Information for " + randName2 + " with email " + email2)

