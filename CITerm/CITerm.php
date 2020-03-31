<?php

class CITerm {
	private
		$_filetype,
		$_filename,
		$_cmd,
		$_error,
		$_types = array("controller", "view", "model");


	function __construct($type = null, $name = null){
		if(!empty($type) && !empty($name)){
			$this->_filetype = $type;
			$this->_filename = $name;
		}
		//read cmd from console & slice it.
		$this->get_cmd();
		//validate sliced cmd (filetype & filename).
		$this->validate_param();
		//Generate the file.
		$this->create_file();
	}

	/**
		* Generate customized MVC file from Template folder.
		* replace the placholder with the classname.
		*
	*/
	private function create_file(){
		$temp_loca = dirname(__FILE__) . "\\Templates\\{$this->_filetype}.php";
		$path = $this->path();
		$template = file_get_contents($temp_loca);
		$template = str_replace("{NAME}", $this->_filename, $template);
		$filename = $path . "\\{$this->_filename}.php";

		if (file_exists($filename)) {
			exit("Warning: {$filename} already exists.\n");
		}
		else{
			$file = fopen($filename, "w") or die("Can't open the file");
			fwrite($file, $template);
	  	fclose($file);
			exit("Success: {$this->_filename}.php has been created.\n");
		}
	}

	/**
		* determin final location of MVC file based on it's type.
		*
		* @return string $path
		*   the path denoting location, where the file will be generated.
	*/
	private function path(){
		$path = dirname(__FILE__);

		if($this->_filetype == "controller"){
			$path .= "\\application\\controllers\\";
		}
		elseif ($this->_filetype == "view") {
			$path .= "\\application\\views\\";
		}
		elseif ($this->_filetype == "model") {
			$path .= "\\application\\models\\";
		}

		return realpath($path);
	}

	/**
		* check for valid cmd and call slice_cmd() to slice it.
		*
	*/
	private function get_cmd(){
		while(empty($this->_filetype) || empty($this->_filename)){
			echo '>>> ';
			$this->_cmd = stream_get_line(STDIN, 1024, PHP_EOL);
			$this->slice_cmd();
		}
	}

	/**
		* slice the cmd into filetype and filename.
		*
		* @return true|false
		*   true if the cmd has been sliced correctly, false otherwise.
		*
	*/
	private function slice_cmd(){
		if(!empty($this->_cmd)){
			$cmd_sliced = explode(" ", $this->_cmd);

			if(count($cmd_sliced) == 2){
				$this->_filetype = $cmd_sliced[0];
				$this->_filename = $cmd_sliced[1];
				return 1;
			}
			else{
				$this->set_error("should Provide 2 paramater. (<Type> <Name>)");
				$this->error();
			}
		}
		return 0;
	}

	/**
		* Apply some validation on filetype & filename variables.
		*
	*/
	private function validate_param(){
		if (!($this->validate_type() && $this->validate_name())){
				$this->error();
				$this->get_cmd();
			}
	}

		/**
			* check for valid filename.
			*
			* @return true|false
			*   true if the filename is valid, false otherwise.
			*
		*/
	private function validate_name(){
		$opt = '/[a-zA-Z\s]*/';
		$reg = array("options" => array("regexp" => $opt));

		if(filter_var($this->_filename, FILTER_VALIDATE_REGEXP, $reg)){
			return 1;
		}

		$this->_filename = null;
		$this->set_error("Filename incorrect.");
		return 0;
	}

	/**
		* check if the type entered match one of the types provided in $_types array.
		*
		* @return true|false
		*   true if the filetype matches, false otherwise.
		*
	*/
	private function validate_type(){
		foreach($this->_types as $it){
			if($it == $this->_filetype)
				return 1;
		}
		$this->_filetype = null;
		$this->set_error("Type incorrect.");
		return 0;
	}

	/**
		* helper string that gets printed whenever there's an error.
		*
	*/
	private function helper(){

		$info = "\n";
		$info .= "Note:\n";
		$info .= "    place CITerm script and Templates folder into your project's main folder\n\n";

		$info .= "Usage:\n";
		$info .= "    php CITerm.php [type] [value]\n\n";

		$info .= "[command]:\n";
		$info .= "    controller            Create a new controller.\n";
		$info .= "    model                 Create a new model.\n";
		$info .= "    view                  Create a new view.\n\n";

		$info .= "[value]:\n";
		$info .= "    Filename              Any valid filename.\n";

		echo $info . "\n";
	}

	/**
		* a setter function to set $_error.
		*
	*/
	private function set_error($msg){
		if(empty($this->_error)){
			$this->_error = $msg;
		}
	}

	/**
		* a printing function to print $_error, call helper() function.
		*
	*/
	private function error(){
			echo "Error : " . $this->_error . "\n";
			$this->_error = null;
			$this->helper();
	}
}

@$cit = new CITerm($argv[1], $argv[2]);
