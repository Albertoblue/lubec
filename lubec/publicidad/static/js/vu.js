new Vue({
    el: '#app6',
    vuetify: new Vuetify(),
    delimiters:['{$','$}'],
    data: {
      message: 'Hello Vue!',
      registro: null,
      contador:0,
    },
    methods:{

      create:function(){
        this.contador+=1;
      
          $("<div>", {
            'class':'btn',
            'id': `f${this.contador}`
            
        }).append($("#detalle").html())
      
        $('#form').append($("<div>", {
          'id': `f${this.contador}`
      }).append($("#detalle").html()));
        
    },

    eliminar:function(){

      if(this.contador==0){
  

        Swal.fire({
          position: 'center',
          icon: 'error',
          title: 'No hay elementos que eliminar',
          showConfirmButton: false,
          timer: 1500
        });
  


      }else{
        $(`#f${this.contador}`).last().remove();
        this.contador-=1;


      }
    
    
      
     
     //$('#modalEdit').modal('show');
     

    }

  }
  
    
  })