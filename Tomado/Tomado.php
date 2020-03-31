<?php
#
# Tomado https://github.com/mohabmes/Tomado
#

require('parsedown.php');

class Tomado{
	private
		$_path,
		$_file,
		$_filename;
	
	
	public function __construct($str, $file, $filename){
		$this->_file = $file;
		$this->_filename = $filename;
		$this->_path = $this->get_dir($str);
		
		$markdown_txt = $this->get_file_content();
		$content = $this->parse($markdown_txt);
		$templ = $this->append_style($content);
		$this->create_file($templ);
	}
	
	private function get_dir($str){
		$path = dirname(realpath($str));
		return $path;
	}
		
	private function get_file_path(){
		$file = $this->_path . "\\" . $this->_file;
		return $file;
	}

	private function generate_filename(){
		$filename = $this->_path . "\\" . $this->_filename;
		return $filename;
	}
	
	function create_file($content){
		$filename = $this->generate_filename() . ".html";
		$file = fopen($filename, "w") or die("Can't open the file");
		fwrite($file, $content);
		fclose($file);
	}

	function parse($markdown_txt){
		$Parsedown = new Parsedown();
		$template = $Parsedown->text($markdown_txt);
		
		return $template;
	}
	
	function get_file_content(){
		$file = $this->get_file_path();
		$content = file_get_contents($file);
		return $content;
	}
	
	function append_style($content){
		$template = file_get_contents("Template\\index.php");
		$template = str_replace("{content}", $content, $template);
		$template = str_replace("{title}", $this->_filename, $template);
		return $template;
	}
}

$obj = new Tomado($argv[0], $argv[1], $argv[2]);