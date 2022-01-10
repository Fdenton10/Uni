**<u>Advanced Topics in Web Development 2 Assignment</u>** 

**<u>Student Name: Francis Denton</u>** 

**<u>Student Number: 18024097</u>**

<u>**XML Processing Models**</u>

XML processing model defines how an application interprets an XML document. This document can be used in a variety of ways, whether to read or write to it, edit the document or create an XML document from scratch are some examples.

The Document object model is a tree like structure where everything inside an XML document is a node. DOM parsing methods load in all of the XML document, allowing for easy navigation and access to any of the individual nodes or elements required. Due to its method of operating being loading in the whole XML document, it is not too suited to handling extremely large files, an example being the original file provided for this assignment potentially. It allows for the construction of complex XML documents and it provides the ability to easily manipulate and modify particular elements when required. using DOM parsing allows for the validation of files using XSD files or being able to query the XML files using XPATH. Unlike XMLWriter(), the DOM API does not require the closing of each element so it allows for multiple uses for information from the XML file.

SimpleXML() is an appropriate method to use when only basic xml editing is required. It is not an appropriate method to use solely if lots of XML files are required to be utilised or generated. This is due to the fact that SimpleXML requires that an XML document already exists in order to work on it. It lacks functions for the removal of existing XML nodes and cannot be used to validate XML with a schema file. 

Streaming parsers differ from DOM parsers as instead of loading the whole xml document, they simply iterate through the document. This makes them more memory efficient. They are more suited to files of a large size which DOM parsing methods might struggled to load or perform slowly with. It operates much faster then its DOM counterpart. The XMLWriter and XML Reader API's are each designed for write-only or read-only respectively, requiring the use of two API's in comparison to the DOM API only requiring the only one. They do not have support for XPATH though they can be used to validate using schema. Every node using XML Writer API needs to be opened with startElement and closed with endElement. A restriction employed by XML Writer is that it disallows for the ability to modify an XML element after it has been added to the structure of an XML document. It is less flexible when creating XML documents as you need to do know all an elements attributes before adding it as the XMLWriter API does not allow editing it later. Streaming parsers do not perform optimally when the XML document is deeply nested.

**Visualisation** 

<img src="C:\Users\Francis\AppData\Roaming\Typora\typora-user-images\image-20210805125352428.png" alt="image-20210805125352428" style="zoom: 33%;" />

<img src="C:\Users\Francis\AppData\Roaming\Typora\typora-user-images\image-20210805125422857.png" alt="image-20210805125422857" style="zoom: 33%;" />

Whilst not the charts required from the spec. I have utilised the google charts API to create a scatter chart and a line chart using data from some of the csv files I have generated.

**Reflection and Learning Outcomes.**

In regards to the first two learning outcomes, tasks 1 and 2 were a great learning experience into this subject area. I have gained an insight into the process of data cleansing. Task 1 required me to break down a large data set into more manageable forms using a divide and conquer strategy. I read in the file, refactored and filtered out any unnecessary elements of the initial data file before writing the newly cleansed data to its appropriate location. I created 18 new files from the cluttered original file, one for each weather station. 

- [Extract-to-csv file](data_files/extract-to-csv.php)
- [Extract-to-csv file (PHPS)](data_files/extract-to-csv.phps)
- [DataFiles(All Files)](data_files)

For task 2, as our file is no longer of an extremely large size as it has been broken down, I utilised the document object model (DOM) to create a new XML document from the existing csv data I had created prior. I created an rootNode tag being 'station' and assigned it with the attributes of the station ID, the station Name and its geocode (Latitude and Longitude numbers). I added records to the XML file where particular data readings were present and created an XML file for each station as required. I created an XSD file to validate the newly generated XML file against my schema. This was tested using the Oxygen XML editor software. Whilst I created a function in my PHP that would do the validation for me, it caused errors as the empty xml file (data_481) would fail the validation so it is left uncalled in the file.

- [Normalise-to-xml](data_files/normalise-to-xml.php)
- [Normalise-to-xml (PHPS)](data_files/normalise-to-xml.phps)
- [XML-Schema](data_files/air-quality.xsd)
- [DataFiles](data_files)

I gained some knowledge into the use of API's, utilising google charts API and [JQuery-csv API](https://github.com/evanplaice/jquery-csv) to create a chart. I called in the data set of a particular file and stored it as an array. Using the functions gathered from the google charts and JQuery API's, I created a line chart and a scatter chart though it was not of the variety that is required in the spec. I was unable to filter the data as required in order to get the output I wanted. Though I have gained knowledge in this area it is still something I need to improve my skills on in order to get the output that is required, it was a good learning experience.

- [Line Chart (Not Correct Chart but displaying that google charts API Functions)](data_files/line_chart.html)
- [Scatter Chart(Not Correct Chart but displaying that google charts API Functions)](data_files/scatter_chart.html)

The submission requirement has been fulfilled. Two conversion files have been submitted, one for csv and one for xml. An XSD File for validation purposes has also been submitted.

I have improved my skills in many different areas. I utilised PHP to create the newly structured csv files. Using those csv files I then created XML files using PHP and DOM parsing. Those xml files were validated with a schema (XSD) file that I created and executed using Oxygen Editor software. I utilised JavaScript and the necessary API's to create a scatter chart and a line chart. I utilised the markdown file format to embed links to my files as required. 

**<u>Code Sources</u>**

[Google Charts](https://developers.google.com/chart/)

[JQuery](https://github.com/evanplaice/jquery-csv)

[W3 DOM](https://www.w3schools.com/php/php_xml_dom.asp)

[W3 XML Schema](https://www.w3schools.com/xml/schema_intro.asp)

[fgets](https://www.php.net/manual/en/function.fgets.php)

[fgetscsv](https://www.php.net/manual/en/function.fgetcsv.php)

