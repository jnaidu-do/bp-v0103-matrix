run ->(env) {
  body = RUBY_VERSION
  [200, {"Content-Type" => "text/plain", "Content-Length" => body.bytesize.to_s}, [body]]
}
