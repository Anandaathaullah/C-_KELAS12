<?php
$conn = mysqli_connect("localhost","root","","sts_Anandaathaullahph");
?>

<!DOCTYPE html>
<html>
<head>
<title>SQL JOIN - STS Anandaathaullahph</title>

<style>

body{
font-family: Arial;
background: #f4f6f8;
text-align:center;
}

h1{
color:#333;
}

.join-box{
width:60%;
margin:30px auto;
background:white;
padding:20px;
border-radius:10px;
box-shadow:0 4px 10px rgba(0,0,0,0.1);
}

.inner{color:#2ecc71;}
.left{color:#3498db;}
.right{color:#e67e22;}
.full{color:#9b59b6;}

table{
width:100%;
border-collapse:collapse;
margin-top:10px;
}

th{
background:#333;
color:white;
padding:10px;
}

td{
padding:8px;
border:1px solid #ccc;
}

tr:hover{
background:#f1f1f1;
}

</style>

</head>
<body>

<h1>SQL JOIN - STS</h1>

<div class="join-box">
<h2 class="inner">INNER JOIN</h2>

<?php
$q = mysqli_query($conn,"
SELECT siswa.nama_siswa, kelas.nama_kelas, jurusan.nama_jurusan
FROM siswa
INNER JOIN kelas ON siswa.id_kelas = kelas.id_kelas
INNER JOIN jurusan ON kelas.id_jurusan = jurusan.id_jurusan
");
?>

<table>
<tr>
<th>Nama Siswa</th>
<th>Kelas</th>
<th>Jurusan</th>
</tr>

<?php while($d=mysqli_fetch_array($q)){ ?>
<tr>
<td><?php echo $d['nama_siswa']; ?></td>
<td><?php echo $d['nama_kelas']; ?></td>
<td><?php echo $d['nama_jurusan']; ?></td>
</tr>
<?php } ?>

</table>
</div>


<div class="join-box">
<h2 class="left">LEFT JOIN</h2>

<?php
$q = mysqli_query($conn,"
SELECT siswa.nama_siswa, kelas.nama_kelas
FROM siswa
LEFT JOIN kelas ON siswa.id_kelas = kelas.id_kelas
");
?>

<table>
<tr>
<th>Nama Siswa</th>
<th>Kelas</th>
</tr>

<?php while($d=mysqli_fetch_array($q)){ ?>
<tr>
<td><?php echo $d['nama_siswa']; ?></td>
<td><?php echo $d['nama_kelas']; ?></td>
</tr>
<?php } ?>

</table>
</div>


<div class="join-box">
<h2 class="right">RIGHT JOIN</h2>

<?php
$q = mysqli_query($conn,"
SELECT siswa.nama_siswa, kelas.nama_kelas
FROM siswa
RIGHT JOIN kelas ON siswa.id_kelas = kelas.id_kelas
");
?>

<table>
<tr>
<th>Nama Siswa</th>
<th>Kelas</th>
</tr>

<?php while($d=mysqli_fetch_array($q)){ ?>
<tr>
<td><?php echo $d['nama_siswa']; ?></td>
<td><?php echo $d['nama_kelas']; ?></td>
</tr>
<?php } ?>

</table>
</div>


<div class="join-box">
<h2 class="full">FULL JOIN</h2>

<?php
$q = mysqli_query($conn,"
SELECT siswa.nama_siswa, kelas.nama_kelas
FROM siswa
LEFT JOIN kelas ON siswa.id_kelas = kelas.id_kelas

UNION

SELECT siswa.nama_siswa, kelas.nama_kelas
FROM siswa
RIGHT JOIN kelas ON siswa.id_kelas = kelas.id_kelas
");
?>

<table>
<tr>
<th>Nama Siswa</th>
<th>Kelas</th>
</tr>

<?php while($d=mysqli_fetch_array($q)){ ?>
<tr>
<td><?php echo $d['nama_siswa']; ?></td>
<td><?php echo $d['nama_kelas']; ?></td>
</tr>
<?php } ?>

</table>
</div>

</body>
</html>