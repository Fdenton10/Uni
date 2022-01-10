<?php
/*
Francis Denton
Student Number - 18024097
Advanced Topics in Web Development 2 - Resit
*/

# Set Timezone
@date_default_timezone_set("GMT");
# Set initial flags required
ini_set('memory_limit','512M');
ini_set('max_execution_time','300');
ini_set('auto_detect_line_endings','TRUE');

#Variable required to confirm number of lines read.
$line_count = 0;
#Variable required to record how long script took to run. Necessary for testing.
$st = microtime(true);

#Open and read in the main file holding all unfiltered and clean data.
$main_file = fopen('air-quality-data-2004-2019.csv', 'r');
#New files for cleaned and filtered data about each individual station.
$data_188 = fopen('data_188.csv', 'w');
$data_203 = fopen('data_203.csv', 'w');
$data_206 = fopen('data_206.csv', 'w');
$data_209 = fopen('data_209.csv', 'w');
$data_213 = fopen('data_213.csv', 'w');
$data_215 = fopen('data_215.csv', 'w');
$data_228 = fopen('data_228.csv', 'w');
$data_270 = fopen('data_270.csv', 'w');
$data_271 = fopen('data_271.csv', 'w');
$data_375 = fopen('data_375.csv', 'w');
$data_395 = fopen('data_395.csv', 'w');
$data_447 = fopen('data_447.csv', 'w');
$data_452 = fopen('data_452.csv', 'w');
$data_459 = fopen('data_459.csv', 'w');
$data_463 = fopen('data_463.csv', 'w');
$data_481 = fopen('data_481.csv', 'w');
$data_500 = fopen('data_500.csv', 'w');
$data_501 = fopen('data_501.csv', 'w');


/*
Data from the original file and the new files need to be displayed in a different format.
$file_headings is the refactored format of the headings.
These headings will need to be written into each file so they are stored as an array.
*/
$file_headings = array('siteID', 'ts', 'nox', 'no2', 'no', 'pm10', 'nvpm10', 'vpm10', 'nvpm2.5', 'pm2.5', 'vpm2.5', 'co', 'o3', 'so2', 'loc', 'lat', 'long');
# fputcsv - formats a line as CSV and writes it to the open files.
# Assigns the newly structured file headings to each of the newly created data files.
fputcsv($data_188, $file_headings);
fputcsv($data_203, $file_headings);
fputcsv($data_206, $file_headings);
fputcsv($data_209, $file_headings);
fputcsv($data_213, $file_headings);
fputcsv($data_215, $file_headings);
fputcsv($data_228, $file_headings);
fputcsv($data_270, $file_headings);
fputcsv($data_271, $file_headings);
fputcsv($data_375, $file_headings);
fputcsv($data_395, $file_headings);
fputcsv($data_447, $file_headings);
fputcsv($data_452, $file_headings);
fputcsv($data_459, $file_headings);
fputcsv($data_463, $file_headings);
fputcsv($data_481, $file_headings);
fputcsv($data_500, $file_headings);
fputcsv($data_501, $file_headings);

# feof = End of file
# While loop which executes until the end of the original data file has been reached.
while (!feof($main_file)) {
	
	/* 
	fgets() = Gets data from current line in file
	$line_data gets set to be the line of data as a string
	Gets reset to data for each line every iteration of the while loop before the end of the file.
	*/ 
	$line_data = fgets($main_file);

	/*
	Break up the original data and assign it to its appropriate variables in an array using the explode method and the delimeter ';'
	Explode function = Breaks a string into an array.
	*/
	[$date_time,$NOx,$NO2,$NO,$siteID,$PM10,$NVPM10,$VPM10,$NVPM2_5,$PM2_5,$VPM2_5,$CO,$O3,$SO2,$Temperature,$RH,$Air_Pressure,$loc,$geo_point_2d] = explode(';', $line_data);
	
	#strtotime = converts text based datetimes into UNIX Timestamps. Required based off of assignment specification
	$unix_time = strtotime($date_time);
	
	#Splits the geographical points into the two required values, latitude being the first value and logitude the second.
	[$lat, $long] = explode(',', $geo_point_2d);

	/*
	Create the new line of data in an array format using the refactored and restructured data set, removing the unnessary elements.
	Unecessary Elements are = Temp, air pressure, relative humidity, date start, date end, current.
	*/
	$line_data = array($siteID, $unix_time, $NOx, $NO2, $NO, $PM10, $NVPM10, $VPM10, $NVPM2_5, $PM2_5, $VPM2_5, $CO, $O3, $SO2, $loc, $lat, $long);
	
	/* 
	IF statement to check whether or not the NOx column or CO Readings are not null.
	Makes sure records have values for either of these columns.
	*/
	if ($line_data[2] != null or $line_data[11] != null) {
	
		/*
		Switch statement which checks the first column of our new refactored line of data.
		As the format of the data has been restructed, the Site ID is the first value in each column.
		Creates a case for each possible idea where it writes the new data to their respective new file.
		fputcsv = writes to the open file
		*/ 
		switch($line_data[0]) {
			
			case 188:
				fputcsv($data_188, $line_data);
				break;
			
			case 203:
				fputcsv($data_203, $line_data);
				break;
			
			case 206:
				fputcsv($data_206, $line_data);
				break;
			
			case 209:
				fputcsv($data_209, $line_data);
				break;
			
			case 213:
				fputcsv($data_213, $line_data);
				break;
			
			case 215:
				fputcsv($data_215, $line_data);
				break;
			
			case 228:
				fputcsv($data_228, $line_data);
				break;
			
			case 270:
				fputcsv($data_270, $line_data);
				break;
			
			case 271:
				fputcsv($data_271, $line_data);
				break;
			
			case 375:
				fputcsv($data_375, $line_data);
				break;
			
			case 395:
				fputcsv($data_395, $line_data);
				break;
			
			case 447:
				fputcsv($data_447, $line_data);
				break;
			
			case 452:
				fputcsv($data_452, $line_data);
				break;
			
			case 459:
				fputcsv($data_459, $line_data);
				break;
			
			case 463:
				fputcsv($data_463, $line_data);
				break;
			
			case 481:
				fputcsv($data_481, $line_data);
				break;
			
			case 500:
				fputcsv($data_500, $line_data);
				break;
			
			case 501:
				fputcsv($data_501, $line_data);
				break;
		}
	
	}
	$line_count++;
}

#Close all of the files that have been opened as no more reads or writes are necessary.
fclose($main_file);
fclose($data_188);
fclose($data_203);
fclose($data_206);
fclose($data_209);
fclose($data_213);
fclose($data_215);
fclose($data_228);
fclose($data_270);
fclose($data_271);
fclose($data_375);
fclose($data_395);
fclose($data_447);
fclose($data_452);
fclose($data_459);
fclose($data_463);
fclose($data_481);
fclose($data_500);
fclose($data_501);

/*Display execution time to make sure it is of the required standard to pass the benchmark test.
ob_clean() = erases the output buffer to prevent it from being sent to the browser.
*/
ob_clean();
echo '<p>Total execution time = ';
echo microtime(true) - $st;
echo ' seconds.<br>';
echo 'Number of lines read from the data file were = '. $line_count .'</p>';
?>