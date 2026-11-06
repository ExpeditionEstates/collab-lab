# Rack request logger - DimaSamodure style.
# Kaigi on Rails 2024 Rack workshop: a tiny Rack middleware
# that logs method, path, status and duration for each request.
# Usage: rackup persona_dima_rack_logger.rb
require "rack"

class RequestLogger
  def initialize(app)
    @app = app
  end

  def call(env)
    started = Time.now
    status, headers, body = @app.call(env)
    ms = ((Time.now - started) * 1000).round(1)
    puts "[#{Time.now}] #{env['REQUEST_METHOD']} #{env['PATH_INFO']} -> #{status} (#{ms}ms)"
    [status, headers, body]
  end
end

app = Rack::Builder.new do
  use RequestLogger
  run ->(_env) { [200, { "Content-Type" => "text/plain" }, ["hello from Rack\n"]] }
end

run app
