<?php
/*
Francis Denton
Student Number - 18024097
Advanced Topics in Web Development 2 - Resit
*/
#Set Variable to track execution time
$st = microtime(true);

#Function called to convert the CSV file to an XML format
#Takes an input of the existing CSV File name and Desired XML filename
function CsvToXml($csv_file, $xml_file) {

    # Open csv file to access elements of it.
	$csv_data  = fopen($csv_file, 'rt');

	#Get the headers of the csv file - will be used to create some of the xml attributes where applicable.
    $headers = fgetcsv($csv_data);
    #Create a new DOM document. Document - Object - Model.
    $xmlDoc  = new DomDocument('1.0',"UTF-8");
    #Set the root element of the DOM to station. Working based off of the example in the specification. Data 447.
    $rootElement = $xmlDoc->createElement('station');
    
    #Perform fgetcsv whilst the file isnt empty.
    #fgetcsv(Takes in a line of the csv as an array)
    while (($data_value = fgetcsv($csv_data)) !== FALSE){
	{
        /*Performs checks neccessary to populate the root attributes
        Necessary XML structure based on specification
        <station id= siteID  name= "location" geocode= lat number , long number> 
        $data_value[0] = siteID column
        $data_value[14] = Location column
        $data_value[15] = latitude column*/
        if ($data_value[0] != null){
            #Create attribute with the value of id in the root node of the xml file (station)
            $rootAttribute = $xmlDoc->createAttribute('id');
            $rootAttribute->value = $data_value[0];
            #After assigning values of the root node attributes we append them to the root node(station).
            $rootElement->appendChild($rootAttribute);
        }
        if($data_value[14] != null){
            #Create attribute with the value of name in the root node of the xml file (station)
            $rootAttribute = $xmlDoc->createAttribute('name');
            #XML treats & as a special character so it must be filtered and replaced where it is found.
            $perform_and_replacement = str_replace('&', ' and ', $data_value[14]);
            $double_quote_check = $perform_and_replacement;
            /*XML does not allowed double quotes to be present inside an element name. 
            Locations name have this so it must be removed in order to be able to be used*/
            $name = str_replace('"', '', $double_quote_check);
            $rootAttribute->value = $name;
            #After assigning values of the root node attributes we append them to the root node(station).
            $rootElement->appendChild($rootAttribute);
        }
        if ($data_value[15] != null){
            #Create attribute with the value of geocode in the root node of the xml file (station)
            $rootAttribute = $xmlDoc->createAttribute('geocode');
            #Concatenate the longitude and latitude numbers once again to form the geocode.
            $geocode = $data_value[15].','.$data_value[16];
            $rootAttribute->value = $geocode;
            #After assigning values of the root node attributes we append them to the root node(station).
            $rootElement->appendChild($rootAttribute);
        
        }	

        #Perform check to see if nox value for the station exists.
        if($data_value[2] != null){
        #Creates the childnode element
        $childNode = $xmlDoc->createElement('rec');
            /*Performs a for loop that loops between the remaining columns of the csv file. From after the site ID until before the Location. 
            We are already using these values in the root node above so we do not need to use them again.
            */
            for ($i = 1; $i < (count($data_value) - 3); $i++){
                    #If their is existing data in that column
                    if($data_value[$i] != null){
                        /*Create an attribute for the child node in the xml document that is equal to the header name from the csv file.
                        #We are not changing names of these attributes unlike with the root node elements so this loop can work effectively.*/
                        $childNodeAttribute = $xmlDoc->createAttribute($headers[$i]);
                        #Assign values based on the index in the csv
                        $childNodeAttribute->value = $data_value[$i];
                        #Append new child node information to the child node
                        $childNode->appendChild($childNodeAttribute);
                    }
                }
                #Append the newly created child node to the root element (station)
                $rootElement->appendChild($childNode);
            }
        }
    }
    #Append the created xml elements to the XML document
    $xmlDoc->appendChild($rootElement);
    #formatOutput = nicely formats the XML file with indentation and extra space.
	$xmlDoc->formatOutput = True;
	$xml = $xmlDoc->saveXML();
	
    #Open the XML file specified in the function calling ready to write the XML into.
	$outputXML = fopen($xml_file, "w");
    #Write too the new file with the created XML
	fwrite($outputXML, $xml);
    #Close the opened files.
	fclose($outputXML);
    fclose($csv_data);
    //validateSchema($xml_file)
}

#Call function for each of the respective files as required. 
CsvToXml("data_188.csv", "data_188.xml");
CsvToXml("data_203.csv", "data_203.xml");
CsvToXml("data_206.csv", "data_206.xml");
CsvToXml("data_209.csv", "data_209.xml");
CsvToXml("data_213.csv", "data_213.xml");
CsvToXml("data_215.csv", "data_215.xml");
CsvToXml("data_228.csv", "data_228.xml");
CsvToXml("data_270.csv", "data_270.xml");
CsvToXml("data_271.csv", "data_271.xml");
CsvToXml("data_375.csv", "data_375.xml");
CsvToXml("data_395.csv", "data_395.xml");
CsvToXml("data_447.csv", "data_447.xml");
CsvToXml("data_452.csv", "data_452.xml");
CsvToXml("data_459.csv", "data_459.xml");
CsvToXml("data_463.csv", "data_463.xml");
CsvToXml("data_481.csv", "data_481.xml");
CsvToXml("data_500.csv", "data_500.xml");
CsvToXml("data_501.csv", "data_501.xml");

/*Function to validate the XML File
#Isn't ran in current version of code as it was taking too long to run properly, too close to benchmark.
#Validation was done manually using Oxygen during testing.
Also caused errors as file data_481 does not fit the schema (Which is allowed in the spec)*/
function validateSchema($xml_file){
    //Creates a new dom doucment and assigns variable to necessary file.
	$xdoc = new DomDocument;
	$xmlfile = $xml_file;
	$xmlschema = 'air-quality.xsd';
	$xdoc -> Load($xmlfile);
    //Validate xml file to the schema
	if($xdoc ->schemaValidate($xmlschema)){
		echo ("$xmlfile is valid.\n");
	}
	else{
		echo("$xmlfile is invalid");
	}
}

#Display Execution time for testing purposes to make sure execution time passes benchmarks set in specification.
echo '<p>Total execution time = ';
echo microtime(true) - $st;
echo ' seconds.<p>';
?>
