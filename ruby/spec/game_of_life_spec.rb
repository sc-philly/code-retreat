require 'game_of_life'

RSpec.describe GameOfLife do
  def live_cell
    double("Cell", living?: true)
  end

  def dead_cell
    double("Cell", living?: false)
  end

  context "Any live cell" do
    let(:cell) { live_cell }

    context "with zero live neighbors" do
      let(:neighbors) { [dead_cell, dead_cell, dead_cell, dead_cell] }

      it "dies, as if by underpopulation." do
        expect(GameOfLife.lives?(cell, neighbors)).to eq(false)
      end
    end
    context "with one live neighbor" do
      let(:neighbors) { [live_cell, dead_cell, dead_cell, dead_cell] }

      xit "dies, as if by underpopulation." do
        expect(GameOfLife.lives?(cell, neighbors)).to eq(false)
      end
    end
    context "with two live neighbors" do
      let(:neighbors) { [live_cell, live_cell, dead_cell, dead_cell] }

      xit "lives on to the next generation." do
        expect(GameOfLife.lives?(cell, neighbors)).to eq(true)
      end
    end
    context "with three live neighbors" do
      xit "lives on to the next generation." do
      end
    end
    context "with four live neighbors" do
      xit "dies, as if by overpopulation." do
      end
    end
  end

  context "Any dead cell" do
    context "with zero live neighbors" do
      xit "remains dead" do
      end
    end
    context "with one live neighbor" do
      xit "remains dead" do
      end
    end
    context "with two live neighbors" do
      xit "remains dead" do
      end
    end
    context "with three live neighbors" do
      xit "becomes a live cell, as if by reproduction." do
      end
    end
    context "with four live neighbors" do
      xit "remains dead" do
      end
    end
  end
end
