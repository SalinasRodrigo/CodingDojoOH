


async function getInfo(){
    var response = await fetch("https://api.github.com/users/adion81")
    var coderData = await response.json();
    console.log(coderData)
    $(".followers").text(coderData['name'] + " has " + coderData['followers'] + " followers. ")
    $(".avatar").attr("src", coderData['avatar_url'] )
    $(".avatar").attr("alt", "avatar adion81")
}
