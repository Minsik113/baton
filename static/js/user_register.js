function checked()
{
    var termchk1=document.getElementById("checkBtn1"); 
    var termchk2=document.getElementById("checkBtn2"); 

    var chk1=termchk1.checked;
    var chk2=termchk2.checked;

    if(chk1==0)
    {
        alert("이용약관에 동의해주세요.");
        termchk1.focus();
        return false;
    }

    else if(chk2==0)
    {
        alert("개인정보수집 및 이용에 동의해주세요.");
        termchk2.focus();
        return false;
    }

    else
    {
        alert("회원가입이 완료되었습니다.");
        return true;
    }
}