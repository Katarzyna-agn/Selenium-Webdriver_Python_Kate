from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//*[text()='Main page' or text()='Strona główna']"
    players_xpath = "//*[text()='Players' or text()='Gracze']"
    change_language_xpath = "//*[text()='English' or text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out' or text()='Wyloguj']"
    players_count_xpath = "//*[text()='Players count' or text()='Ilość graczy']"
    matches_count_xpath = "//*[text()='Matches count' or text()='Ilość meczy']"
    reports_count_xpath = "//*[text()='Reports count' or text()='Ilość raportów']"
    events_count_xpath = "//*[text()='Events count' or text()='Ilość akcji']"
    dev_team_contact_xpath = "//*[text()= 'Dev team contact']"
    add_player_xpath = "//*[text()='Add player' or text()='Dodaj gracza']"
    activity_xpath = "//*[text()='Activity' or text()='Aktywnosć']"
    last_created_player_xpath = "//div/div/h6[1]"
    last_updated_player_xpath = "//div/div/h6[2]"
    last_created_match_xpath = "//div/div/h6[3]"
    last_updated_match_xpath = "//div/div/h6[4]"
    last_updated_report_xpath = "//div/div/h6[5]"


pass
