from selenium.webdriver.common.by import By

locator = {
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'class': By.CLASS_NAME,
    'css_selector': By.CSS_SELECTOR
}

locator_path = {
    'drop_down_menu': 'searchDropdownBox',
    'search_box': 'twotabsearchtextbox',
    'search_result': '//*[@id="search"]/span/div',
    'original_text': 'The Secret of The Nagas (Shiva Trilogy Book 2) (Shiva, 2) Paperback by Amish Tripathi (Author), By All Books Centre',
    'partial_text_for_book': 'The Secret of The Nagas (Shiva Trilogy Book 2) (Shiva, 2)',
    'book_price': 'price',
    'original_price': 'listPrice',
    'discount': 'savingsPercentage'
}
