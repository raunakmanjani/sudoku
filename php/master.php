<?php 
	
	$in = $_GET['puzzle'];
	$con=mysqli_connect("localhost","pydoku1","su4086","sudoku");
	if (mysqli_connect_errno()) {
		echo '{"status":"DB Connection Error"}';
		mysqli_close($con);	
		exit();
	}	
	$in = strip_tags(mysqli_real_escape_string($con,$in));
	if(strlen($in)!=81){
		echo '{"status":"Invalid Length"}';
		exit();
	}
	$in = preg_replace('/[^0-9\-]/', '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000', $in);
	if(strlen($in)!=81){
		echo '{"status":"Invalid Symbols Used"}';
		mysqli_close($con);	
		exit();
	}

	// check if already exists

	$result = mysqli_query($con,"SELECT ot FROM masty where data = '".$in."'");
	while($row = mysqli_fetch_array($result)) {
		$ret = $row['ot'];
		if($ret=="0")
			echo '{"status":"Computing Now"}';
		else if($in==$ret)
			echo '{"status":"Invalid/Wrong Puzzle"}';
		else
			echo '{"status":"Success","ctext":"'.$ret.'"}';	
		mysqli_close($con);	
		exit();		
	}

	// if not exists - insert

	if(mysqli_query($con,"Insert into masty(data) values('".$in."')"))
		echo '{"status":"Queued for Computation"}';	
	mysqli_close($con);	
?>