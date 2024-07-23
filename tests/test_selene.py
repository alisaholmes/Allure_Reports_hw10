from selene import browser, by, be


def test_github():
    browser.open("/")
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("alisaholmes/Allure_Reports_hw10").press_enter()
    browser.element(by.link_text("alisaholmes/Allure_Reports_hw10")).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("Welcome to issues!")).should(be.visible)
