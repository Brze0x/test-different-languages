from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_cart_button(browser):
    browser.get(link)
    basket_btn = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket_btn, "Add to basket button not found"
