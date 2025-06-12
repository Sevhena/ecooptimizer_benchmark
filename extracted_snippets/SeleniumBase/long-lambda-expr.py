# long-lambda-expr snippets for SeleniumBase

# File: /root/ecooptimizer/SeleniumBase/seleniumbase/console_scripts/sb_caseplans.py
# Line: 452

command=lambda: generate_case_plan_boilerplates(
    root,
    tests,
    ara,
    tests_with_case_plan,
    tests_without_case_plan,
),

# ==================================================
# File: /root/ecooptimizer/SeleniumBase/seleniumbase/core/browser_launcher.py
# Line: 5473

driver.get = lambda url: uc_special_open_if_cf(
    driver,
    url,
    proxy_string,
    mobile_emulator,
    device_width,
    device_height,
    device_pixel_ratio,
)

# ==================================================
