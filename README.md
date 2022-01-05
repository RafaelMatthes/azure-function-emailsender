<h1> Azure Function - Email Sender </h1>

<p> This is a simple function to "simulate a verification" of a new user's email account. </p>

* Only works with a gmail account.
* Only accepts POST requests.

<h3>Add to Application settings:</h3>
<ul>
  <li> "EMAIL": "< your email account >@gmail.com" </li>
  <li> "PASSWORD": "< password >" </li>
</ul>

<h3>Params:</h3>
<ul>
     <li> code: < Azure token > </li>
     <li> receiver_email : < must be a valid email > </li>
     <li> link : < must inform a link to redirect user > </li>
     <li> aditional_text : < optional text > </li>
     <li> html_text : < custom html message > </li>
     
 </ul>
