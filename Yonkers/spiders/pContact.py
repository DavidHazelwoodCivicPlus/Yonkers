import scrapy


class PcontactSpider(scrapy.Spider):

    # Name of the file adn what you call to run this script
    name = "pContact"

    # Allowed domains this script can scrape
    allowed_domains = ["www.yonkersny.gov"]

    # Starting URL the script will get info from. 
    start_urls = ["https://www.yonkersny.gov/government/departments/purchasing/contact"]

    def parse(self, response):

        # content should be set to whatever is holding the group of contact information
        content = response.css('.clearfix p')
        for contact in content :

            # This makes sure that the Excel file for staff import is created and has nothing inside by default.
            # Hardcode the values you want to be passed into the archive.
            firstName = 'First'
            lastName = 'Last'
            title = ''
            phone = ''
            email = contact.xpath('//a[contains(@href, "mailto")]/@href').get()
            showEmail = '' # This dosen't need to be hardcoded and will be created based on the first and last name if there is any emails scrapped
            link = ''
            linkText = ''
            biography = ''
            showArchive = 'False' # Never seen "Show Archive" to be anything other than "False"
            department = ''

            if(email != '') :
                showEmail = 'Email ' + firstName + ' ' + lastName
        
            # Everything in the yield section does not need to be touched.
            yield {
                'First Name' : firstName,
                'Last Name' : lastName,
                'Title' : title,
                'Phone' : phone,
                'Email' : email,
                'Show Email' : showEmail,
                'Link' : link,
                'Link Text' : linkText,
                'Biography' : biography,
                'Show Archive' : showArchive,
                'Department' : department,
            }
