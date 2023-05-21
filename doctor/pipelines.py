# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class DoctorPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Clean and process the 'Name' field
        adapter['name'] = adapter.get('name', '').strip()

        # Clean and process the 'Title' field
        adapter['title'] = adapter.get('title') and adapter.get('title').strip()

        # Clean and process the 'Gender' field
        gender = adapter.get('gender')
        adapter['gender'] = gender.strip() if gender else None

        # Clean and process the 'Expertise' field
        expertise = adapter.get('expertise')
        adapter['expertise'] = expertise.strip() if expertise else None

        # Clean and process the 'Research' field
        #research = adapter.get('research', '')
        #hidden_text = ''.join(re.findall(r'[a-zA-Z]+', research))
        #research = re.sub(r'\s+', ' ', research + hidden_text).strip() or None
        #adapter['research'] = research

        # Clean and process the 'Research' field
        research = adapter.get('research', '')
        adapter['research'] = research.strip() if research else None
        #hidden_text = ''.join(re.findall(r'\b[a-zA-Z]+\b', research))
        #adapter['research'] = re.sub(r'\s+', ' ', research + hidden_text).strip() or None


        # Clean and process the 'Phone' field
        phone = adapter.get('phone')
        if phone:
            phone = phone.strip()
            fax = re.search(r'Fax: (\d+)', phone)
            if fax:
                phone = f"Phone: {fax.group(1)}"
            adapter['phone'] = re.sub(r'\s+', ' ', phone)
        else:
            adapter['phone'] = None


        # Clean and process the 'Location' field
        adapter['location'] = re.sub(r'\s+', ' ', adapter.get('location', '').strip())

        # Clean and process the 'Education' field
        education = [edu.strip() for edu in adapter.get('education', []) if edu and edu.strip()]
        adapter['education'] = education or None


        return item
