def observe(page_content):
    print("📋 Checking if enough information was found...")

    if len(page_content.strip()) > 1000:
        return True, "Enough information collected"

    return False, "Information is still insufficient"