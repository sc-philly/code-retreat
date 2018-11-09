require 'hello'

RSpec.describe Hello do
  let(:kenya) { double("Person", name: "Kenya") }

  it "says hello" do
    expect(subject.hello(kenya)).to eql("Hello, Kenya!")
  end
end
