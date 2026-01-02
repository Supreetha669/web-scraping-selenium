def extract_jobs(jobs):
    data = []
    for job in jobs:
        title = job.find_element("tag name", "h2").text
        company = job.find_element("class name", "company").text
        location = job.find_element("class name", "location").text
        link = job.find_element("tag name", "a").get_attribute("href")
        data.append([title, company, location, link])
    return data
