<?php
require_once 'login.php';
$conn = new mysqli($db_hostname, $db_username, $db_password, $db_database);
// users can use the objects in module directly
if ($conn->connect_error) die($conn->connect_error);

$query = "SELECT * FROM pet";
$result = $conn->query($query); // pay attention to this function 'query'
if (!$result) die($conn->error);

$rows = $result->num_rows; // return the number of rows in $result

echo "<pre>";
for ($j=0; $j<$rows; ++$j)
{
		$result->data_seek($j);
		$row = $result->fetch_array(MYSQLI_ASSOC);
		// return all data in one row as the type 'array'

		echo 'Name:' . $row['name'] . '<br>';
		echo 'Owner:' . $row['owner'] . '<br>';
		echo 'Sex:' . $row['sex'] . '<br>';
		echo 'Birth:' . $row['birth'] . '<br>';
		echo 'Death:' . $row['death'] . '<br><br>';
}
/*
for ($j=0; $j<$rows; ++$j)
		echo 'Name:' . $rows['name'] / '<br>';
		$result->data_seek($j);
		echo 'Name:' . $result->fetch_assoc()['name'] . '<br>';
		// return all data in one row as the type 'array'
		$result->data_seek($j);
		echo 'Owner:' . $result->fetch_assoc()['owner'] . '<br>';
		$result->data_seek($j);
		echo 'Birth:' . $result->fetch_assoc()['birth'] . '<br>';
		$result->data_seek($j);
		echo 'Sex:' . $result->fetch_assoc()['sex'] . '<br>';
		$result->data_seek($j);
		echo 'Death:' . $result->fetch_assoc()['death'] . '<br><br>';
}
// pay attention to the function 'data_seek' and 'fetch_assoc'
// */

$result->data_seek(2);
print_r($result->fetch_array(MYSQLI_BOTH));
echo "</pre>";

$result->close();
$conn->close();
?>
