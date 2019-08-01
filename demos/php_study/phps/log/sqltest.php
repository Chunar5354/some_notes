<?php
require_once 'login.php';
$conn = new mysqli($db_hostname, $db_username, $db_password, $db_database);
if ($conn->connect_error) die($conn->connect_error);

if (isset($_POST['delete']) && isset($_POST['birth']))
{
		$birth = get_post($conn, 'birth');
		$query = "DELETE FROM pet WHERE birth='$birth'";
		$result = $conn->query($query);
		if (!$result) echo "DELETE failed: $query<br>" . $conn->error . "<br><br>";
}

if (isset($_POST['name']) &&
	isset($_POST['owner']) &&
	isset($_POST['species']) &&
	isset($_POST['sex']) &&
	isset($_POST['birth']) &&
	isset($_POST['death']))
{
		$name = get_post($conn, 'name');
		$owner = get_post($conn, 'owner');
		$species = get_post($conn, 'species');
		$sex = get_post($conn, 'sex');
		$birth = get_post($conn, 'birth');
		$death = get_post($conn, 'death');

		$query = "INSERT INTO pet VALUES" . 
				"('$name', '$owner', '$species', '$sex', '$birth', '$death')";
		$result = $conn->query($query);
		if (!$result) echo "INSERT dailed: $query<br>" . 
				$conn->error . "<br><br>";
}

echo <<<_END
<form action="sqltest.php" method="post"><pre>
Name <input type="text" name="name">
Owner <input type="text" name="owner">
Species <input type="text" name="species">
Sex <input type="text" name="sex">
Birth <input type="text" name="birth">
Death <input type="text" name="death">
<input type="submit" value="ADD RECORD">
</pre></form>
_END;

$query = "SELECT * FROM pet";
$result = $conn->query($query);
if (!$result) die("Database access failed:" . $conn->error);

$rows = $result->num_rows;

for ($j=0; $j<$rows; ++$j)
{
		$result->data_seek($j);
		$row = $result->fetch_array(MYSQLI_NUM);

		echo <<<_END
		<pre>
		Name $row[0]
		Owner $row[1]
		Species $row[2]
		Sex $row[3]
		Birth $row[4]
		Death $row[5]
		</pre>
		<form action="sqltest.php" method="post">
		<input type="hidden" name="delete" value="yes">
		<input type="hidden" name="birth" value="$row[4]">
		<input type="submit" value="DELETE RECORD">
		</form>
_END;
}

$result->close();
$conn->close();

function get_post($conn, $var)
{
		print_r($_POST);
		return $conn->real_escape_string($_POST[$var]);
}
?>
