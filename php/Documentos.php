<?php 

class Documentos{

    // private $mascara = '000.000.000-00';

    protected $cpf = '';

    const MASCARA = '000.000.000-00';

    public function getCpf(){
        return $this->cpf;
    }

    protected function validaCpf($cpf){
        if(strlen($cpf) == 14){
            return $cpf;
        }
        else{
            return 'Aviso: Você digitou o seguinte CPF: "'.$cpf.'". Este valor é inválido. Digite o CPF da seguinte forma: '.Documentos::MASCARA.'<br>';
        }
    }

    public function setCpf($cpf){

        $this->cpf = Documentos::validaCpf($cpf);

    }

}
