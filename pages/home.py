#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class HomePage(BasePage):

    _page_title = 'Mozilla Developer Network'
    _display_name_locator = (By.CSS_SELECTOR, '.user-state > ul > li:nth-child(1) > a')

    def go_to_page(self):
        self._go_to_page('/')

    @property
    def display_name(self):
        return self.selenium.find_element(*self._display_name_locator).get_attribute('text')
