var password=document.querySelector(".password");
var names=document.querySelector(".name");
var p=document.querySelector(".pass_see");
var finish=document.querySelector(".finish");
var noict=document.querySelector(".noict");
p.onclick=function(){
    if(password.type=='password'){
        password.type='text';
    }else{
        password.type='password';
    }
}
finish.onclick=function(){
    //alert(names.value);
    $.get("/登陆.html",{"password":password.value,"name":names.value},function(result){
        //alert(result)
        if(result=="1"){
            alert("登陆成功");
            noict.innerHTML=("登陆成功 点我返回");
        }if(result=="2"){
            alert("改用户名下的密码错误，该账号已被注册或密码错误");
            noict.innerHTML=("");
        }if(result=="3"){
            alert("检测不到该账号\n已自动为您注册");
            noict.innerHTML=("注册成功 点我返回");
        }if(result=="4"){
            alert("当前未找到账号 自动为您注册新账号\n但注册的密码过于短小精悍 请将其长度设置在6位以上")
        }
        //alert(String(result));
         console.log('注册',result);
        // noict.innerHTML=(String(result));
    },"json")
}