from bs4 import BeautifulSoup
import requests
import datetime


def get_tech_jobs():
    jobs = []
    """
        Scrapes tech posted tech jobs from Elevolt
    """
    try:

        for i in range(1, 10):
            url = "https://www.elevolt.co.ke/jobs?page={}&location=&skill=software_it&type=&qualification=&search=".format(
                i
            )
            r = requests.get(url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, "html5lib")
                title = soup.findAll("h3", {"class": "text-base"})  # get job titile
                company = soup.findAll("h5")[2:]  # Get company name
                # print(soup)
                for title, company in zip(title, company):
                    job = {
                        "company": company.span.contents[0],
                        "position": title.contents[0],
                    }
                    jobs.append(job)
                    # print(title, company, "====================================")
    except Exception as ex:
        print("Exception in get_tech_jobs")
        print(str(ex))
    finally:
        return jobs
