# Homebrew formula scaffold for Ledger
# Tap: ledger-org/tap
class Ledger < Formula
  include Language::Python::Virtualenv

  desc "Production-grade database backup orchestration"
  homepage "https://github.com/ledger-org/ledger"
  url "https://github.com/ledger-org/ledger/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "PLACEHOLDER_SHA256"
  license "MIT"

  depends_on "python@3.12"
  depends_on "postgresql@16" => :optional
  depends_on "mysql-client" => :optional

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "ledger", shell_output("#{bin}/ledger --version")
  end
end
