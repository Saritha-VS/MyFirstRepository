from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://facebook.com")
browser.find_element_by_id("email").send_keys("username")
browser.find_element_by_id("pass").send_keys("password")
browser.find_element_by_id("loginbutton").click()
browser.implicitly_wait(10)

for i in browser.window_handles:
	browser.switch_to_window(i)
	if(browser.title == "Facebook"):
		print"switch_to_window"
		break;