import secret
from selenium import webdriver

driver = webdriver.Firefox()

# Login
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys(secret.EMAIL)
driver.find_element_by_id("pass").send_keys(secret.PASSWORD)
driver.find_element_by_id("loginbutton").click()

driver.get("https://www.facebook.com/photo.php?fbid=1927413537286251&set=gm.822438591292710")
driver.find_element_by_class_name("layerCancel").click()  # Remove active notification pop-up
a = driver.find_elements_by_tag_name("a")
for link in a:
    print(link.text)
# driver.close()