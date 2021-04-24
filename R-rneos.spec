#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rneos
Version  : 0.4.0
Release  : 22
URL      : https://cran.r-project.org/src/contrib/rneos_0.4-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rneos_0.4-0.tar.gz
Summary  : XML-RPC Interface to NEOS
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RCurl
Requires: R-XML
BuildRequires : R-RCurl
BuildRequires : R-XML
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n rneos
cd %{_builddir}/rneos

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589538398

%install
export SOURCE_DATE_EPOCH=1589538398
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rneos
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rneos
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rneos
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rneos || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rneos/DESCRIPTION
/usr/lib64/R/library/rneos/ExAMPL/diet.dat
/usr/lib64/R/library/rneos/ExAMPL/diet.mod
/usr/lib64/R/library/rneos/ExGAMS/TwoStageStochastic.gms
/usr/lib64/R/library/rneos/INDEX
/usr/lib64/R/library/rneos/Meta/Rd.rds
/usr/lib64/R/library/rneos/Meta/features.rds
/usr/lib64/R/library/rneos/Meta/hsearch.rds
/usr/lib64/R/library/rneos/Meta/links.rds
/usr/lib64/R/library/rneos/Meta/nsInfo.rds
/usr/lib64/R/library/rneos/Meta/package.rds
/usr/lib64/R/library/rneos/NAMESPACE
/usr/lib64/R/library/rneos/R/rneos
/usr/lib64/R/library/rneos/R/rneos.rdb
/usr/lib64/R/library/rneos/R/rneos.rdx
/usr/lib64/R/library/rneos/help/AnIndex
/usr/lib64/R/library/rneos/help/aliases.rds
/usr/lib64/R/library/rneos/help/paths.rds
/usr/lib64/R/library/rneos/help/rneos.rdb
/usr/lib64/R/library/rneos/help/rneos.rdx
/usr/lib64/R/library/rneos/html/00Index.html
/usr/lib64/R/library/rneos/html/R.css
