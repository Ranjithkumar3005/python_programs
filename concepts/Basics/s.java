private void jButton5ActionPerformed(java.awt.event.ActionEvent evt) {
// TODO add your handling code here:
int amount = Integer.parseInt(amounttf.getText());
if(amount >=50000)
{
JOptionPane.showMessageDialog(null,"Amount is greater than 50000");
JOptionPane.showMessageDialog(null,"Logout to try again");
this.setVisible(false);
ATM atm = new ATM();
atm.setVisible(true);
}
else if(amount <=50)
{
JOptionPane.showMessageDialog(null,"Amount is too low to deposit");
JOptionPane.showMessageDialog(null,"Logout to try again");
this.setVisible(false);
ATM atm = new ATM();
atm.setVisible(true);
}
else if(amounttf.getText().isEmpty() || amounttf.getText().equals(0))
{
JOptionPane.showMessageDialog(null,"Enter a Valid Amount");
}
else
{
try
{
Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/signup","root","root");
Statement ps=con.createStatement();
int deposit;
String qry="SELECT * FROM data where AccountNumber= ' " + AccMyNum + " ' ";
ResultSet rs = ps.executeQuery(qry);
if(rs.next())
{
int balance=rs.getInt("Balance");
int temp = balance +amount ;
String strSQL = "UPDATE data set Balance = ' " + (temp) + " ' where AccountNumber= ' "+ AccMyNum + " ' ";
int rowsEffected = ps.executeUpdate(strSQL);
if(rowsEffected == 0)
{
JOptionPane.showMessageDialog(null,"Amount not Deposited");
}
else
{
JOptionPane.showMessageDialog(null,"Amount Deposited Successfully");
amounttf.setText("");
Transaction t=new Transaction(AccMyNum,Name);
t.setVisible(true);
dispose();
timer.stop();
}
}
con.close();
ps.close();
rs.close();
}
catch(Exception e)
{
JOptionPane.showMessageDialog(null,e);
}
}
}

