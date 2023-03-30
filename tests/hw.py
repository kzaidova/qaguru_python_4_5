from selene import browser
from selene import be, have, command
import os

def test_fil_and_submit_form(open_and_close_browser):
    #interfering removal
    browser.element('[id="adplus-anchor"]').perform(command.js.remove)
    browser.element('[id="close-fixedban"]').perform(command.js.remove)
    browser.element('footer').perform(command.js.remove)

    browser.element('[id="firstName"]').should(be.blank).type('Катрин')
    browser.element('[id="lastName"]').should(be.blank).type('Заидова')
    browser.element('.col-md-9 [id="userEmail"]').should(be.blank).type('newemail@mail.ru')
    browser.element('[for="gender-radio-2"]').should(be.clickable).click()
    browser.element('.col-md-9 [id="userNumber"]').should(be.blank).type('9998076767')
    browser.element('[id="dateOfBirthInput"]').should(be.clickable).click()
    browser.element('.react-datepicker__year-select').type('1995')
    browser.element('.react-datepicker__month-select').type('August')
    browser.element(f'.react-datepicker__day--0{24}').should(be.clickable).click()
    browser.element('[id="subjectsInput"]').should(be.blank).click()
    browser.element('[id="subjectsInput"]').type('Eng').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('../bear.jpg'))
    browser.element('[id="currentAddress"]').should(be.blank).type('Koh Samui, Thailand')
    browser.element('#state').should(be.clickable).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text("Haryana")).should(be.clickable).click()
    browser.element('#city').should(be.clickable).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text("Karnal")).should(be.clickable).click()
    browser.element('[id="submit"]').should(be.clickable).click()



