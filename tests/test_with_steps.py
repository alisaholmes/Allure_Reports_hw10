from selene import browser, by, be
import allure


def test_with_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("/")
    with allure.step("Ищем репозиторий и переходим в него"):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element("#query-builder-test").send_keys("alisaholmes/Allure_Reports_hw10").press_enter()
        browser.element(by.link_text("alisaholmes/Allure_Reports_hw10")).click()
    with allure.step("Открываем Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Проверяем наличие в Issues текста Welcome to issues!"):
        browser.element(by.partial_text("Welcome to issues!")).should(be.visible)




