$(document).ready(()=>{
     $(document).on("submit","form.ajax",function(e){
        e.preventDefault();
        var $this=$(this);
        var action=$this.attr("action");
        var method=$this.attr("method");
        $.ajax({
            type:method,
            url:action,
            dataType:"json",
            data:new FormData(this),
            processData:false,
            contentType:false,
            cache:false,
            success:(data)=>{
                let status=data["status"];
                let title=data["title"];
                let message=data["message"];
                Swal.fire({
                    icon: status,
                    title: title,
                    text: message
                }).then((result)=>{
                    location.reload();
                });
                if (status == "success"){
                    $this.trigger("reset");
                }
            },
            error:(error)=>{
                console.log("error")
            }
        })
    })

    $(document).on("submit","form.confirm",function(e){
        e.preventDefault();
        if(confirm("Are you sure?    Once you deleted it can't revert again!!")){
            var $this=$(this);
            var action=$this.attr("action");
            var method=$this.attr("method");
            $.ajax({
                type:method,
                url:action,
                dataType:"json",
                data:new FormData(this),
                processData:false,
                contentType:false,
                cache:false,
                success:(data)=>{
                    let status=data["status"];
                    let title=data["title"];
                    let message=data["message"];
                    Swal.fire({
                        icon: status,
                        title: title,
                        text: message
                    }).then((result)=>{
                        location.reload();
                    });
                    if (status == "success"){
                        $this.trigger("reset");
                    }
                },
                error:(error)=>{
                    console.log("error")
                }
            })
        }
    })
    
    $(document).on("submit","form.update",function(e){
        e.preventDefault();
        var $this=$(this);
        var action=$this.attr("action");
        var method=$this.attr("method");
        $.ajax({
            type:method,
            url:action,
            dataType:"json",
            data:new FormData(this),
            processData:false,
            contentType:false,
            cache:false,
            success:(data)=>{
                let status=data["status"];
                let title=data["title"];
                let message=data["message"];
                Swal.fire({
                    icon: status,
                    title: title,
                    text: message
                }).then((result)=>{
                    location.href='http://127.0.0.1:8000/index';
                });
                if (status == "success"){
                    $this.trigger("reset");
                }
            },
            error:(error)=>{
                console.log("error")
            }
        })
    })
    
})
