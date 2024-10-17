Name:		texlive-hvextern
Version:	70795
Release:	1
Summary:	Write and execute external code, and insert the output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hvextern
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvextern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvextern.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to write MetaPost, TeX, ConTeXt, LaTeX,
LuaTeX, LuaLaTeX, XeTeX, XeLaTeX, Lua, Perl, or Python source
code into an external file, run that file via shell-escape to
create PDF, PNG, or text output, and include that output
automatically into the main LaTeX document.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hvextern
%doc %{_texmfdistdir}/doc/latex/hvextern

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
