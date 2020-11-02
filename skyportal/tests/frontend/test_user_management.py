import pytest


def test_delete_user_role(driver, super_admin_user, user):
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/user_management')
    driver.click_xpath(
        f"//div[@id='deleteUserRoleButton_{user.id}_Full user']//*[contains(@class, 'MuiChip-deleteIcon')]"
    )
    driver.wait_for_xpath(f"//div[text()='User role successfully removed.']")
    driver.wait_for_xpath_to_disappear(
        f"//div[@id='deleteUserRoleButton_{user.id}_Full user']//*[contains(@class, 'MuiChip-deleteIcon')]"
    )


def test_grant_and_delete_user_acl(driver, super_admin_user, user):
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/user_management')
    driver.click_xpath(f'//*[@data-testid="addUserACLsButton{user.id}"]')
    driver.click_xpath('//*[@id="addUserACLsSelect"]')
    driver.click_xpath('//li[text()="Annotate"]')
    driver.click_xpath('//*[text()="Submit"]')
    driver.wait_for_xpath('//*[text()="User successfully granted specified ACL(s)."]')
    driver.click_xpath(
        f"//div[@id='deleteUserACLButton_{user.id}_Annotate']//*[contains(@class, 'MuiChip-deleteIcon')]"
    )
    driver.wait_for_xpath(f"//div[text()='User ACL successfully removed.']")
    driver.wait_for_xpath_to_disappear(
        f"//div[@id='deleteUserACLButton_{user.id}_Annotate']//*[contains(@class, 'MuiChip-deleteIcon')]"
    )


def test_add_user_role(driver, super_admin_user, user):
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/user_management')
    driver.click_xpath(f'//*[@data-testid="addUserRolesButton{user.id}"]')
    driver.click_xpath('//*[@id="addUserRolesSelect"]')
    driver.click_xpath('//li[text()="Group admin"]')
    driver.click_xpath('//*[text()="Submit"]')
    driver.wait_for_xpath('//*[text()="User successfully granted specified role(s)."]')
    driver.wait_for_xpath(
        f"//div[@id='deleteUserRoleButton_{user.id}_Group admin']//*[contains(@class, 'MuiChip-deleteIcon')]"
    )


def test_delete_group_user(driver, super_admin_user, user, public_group):
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/user_management')
    driver.wait_for_xpath(
        f"//div[@id='deleteGroupUserButton_{user.id}_{public_group.id}']"
    )
    driver.click_xpath(
        f"//div[@id='deleteGroupUserButton_{user.id}_{public_group.id}']//*[contains(@class, 'MuiChip-deleteIcon')]"
    )
    driver.wait_for_xpath(
        f"//div[text()='User successfully removed from specified group.']"
    )


@pytest.mark.flaky(reruns=2)
def test_delete_stream_user(driver, super_admin_user, user, stream_with_users):
    stream = stream_with_users
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/user_management')
    driver.wait_for_xpath(f"//div[@id='deleteStreamUserButton_{user.id}_{stream.id}']")
    driver.click_xpath(
        f"//div[@id='deleteStreamUserButton_{user.id}_{stream.id}']//*[contains(@class, 'MuiChip-deleteIcon')]"
    )
    driver.wait_for_xpath(f"//div[text()='Stream access successfully revoked.']")


def test_add_user_to_group(driver, user, super_admin_user, public_group, public_group2):
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/user_management')
    driver.wait_for_xpath(
        f"//div[@id='deleteGroupUserButton_{user.id}_{public_group.id}']"
    )
    driver.click_xpath(f'//*[@data-testid="addUserGroupsButton{user.id}"]')
    driver.click_xpath('//*[@id="addUserToGroupsSelect"]')
    driver.click_xpath(f'//li[text()="{public_group2.name}"]')
    driver.click_xpath('//*[text()="Submit"]')
    driver.wait_for_xpath(
        '//*[text()="User successfully added to specified group(s)."]'
    )
    driver.wait_for_xpath(
        f"//div[@id='deleteGroupUserButton_{user.id}_{public_group2.id}']"
    )


def test_add_user_to_stream(
    driver, user, super_admin_user, public_group, public_stream, public_stream2
):
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/user_management')
    driver.wait_for_xpath(
        f"//*[@id='deleteGroupUserButton_{user.id}_{public_group.id}']"
    )
    driver.click_xpath(f'//*[@data-testid="addUserStreamsButton{user.id}"]')
    driver.click_xpath('//*[@id="addUserToStreamsSelect"]')
    driver.click_xpath(f'//li[text()="{public_stream2.name}"]')
    driver.click_xpath('//*[text()="Submit"]')
    driver.wait_for_xpath(
        '//*[text()="User successfully added to specified stream(s)."]'
    )
    driver.wait_for_xpath(
        f"//div[@id='deleteStreamUserButton_{user.id}_{public_stream2.id}']"
    )
